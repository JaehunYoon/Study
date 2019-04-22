#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <fentl.h>
#include <errno.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/stat.h>

int main(int argc, char *argv[]) {
    int fd, sz_page;
    char *p_map;
    struct stat stat_buf;

    if (argc != 2) {
        printf("Usage : %s <mmap file>\n", argv[0]);
        return EXIT_FAILURE;
    }
    printf("System Page Size = %d\n", (sz_page = sysconf(_SC_PAGESIZE)));

    fd = open(argv[1], O_RDWR|O_CREAT, 0664);

    if (fd == -1) {
        printf("Fail: open() : (%d:%s)\n", errno, strerror(errno));
        return EXIT_FAILURE;
    }

    if (fstat(fd, &stat_buf) == -1) {
        printf("Fail: fstat(): (%d:%s)\n", errno, strerror(errno));
        return EXIT_FAILURE;
    }

    if (stat_buf.st_size < sz_page) {
        ftruncate(fd, sz_page);
    }

    p_map = mmap((void *)0, 64, PROT_READ|PROT_WRITE, MAP_SHARED, fd, 0);

    if (p_map == MAP_FAILED) {
        printf("Fail: mmap(): (%d:%s)\n", errno, strerror(errno));
        return EXIT_FAILURE;
    }

    sprintf(p_map, "%s", "Testing synchronized mmap.\n");

    // synchronizing mmap
    printf(">> Synchronizing Memory Mapped File.\n");
    if (msync(p_map, 64, MS_SYNC) == -1) {
        printf("Fail: msync(): (%d:%s)\n", errno, strerror(errno));
        return EXIT_FAILURE;
    }

    printf(">> Unmapping Memory Mapped File.\n");
    if (munmap(p_map, 64) == -1) {
        printf("Fail: munmap(): (%d:%s)\n", errno, strerror(errno));
        return EXIT_FAILURE;
    }

    if (fsync(3) == -1) {
        printf("Fail: fsync(): (%d:%s)\n", errno, strerror(errno));
        return EXIT_FAILURE;
    }

    printf(">> Closing File.\n");
    close(fd);

    return EXIT_SUCCESS;
}