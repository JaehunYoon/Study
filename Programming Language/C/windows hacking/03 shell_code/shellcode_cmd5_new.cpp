#include <stdio.h>
#include <tchar.h>

int _tmain(int argc, _TCHAR* argv[])
{
	__asm {
		jmp start

		get_func_addr :

		// get name table index
	loop_ent:
		inc edx			// index++
			lodsd			// eax = *esi , esi += 4
			pushad
			add	ebx, eax
			mov	esi, ebx
			xor eax, eax
			xor edi, edi
			hash :
		lodsb			// eax = *esi, esi += 1   
			add edi, eax	// edi += char
			test al, al
			jnz hash

			mov[ebp + 0x10], edi
			popad
			cmp[ebp + 0x10], edi // cmp export name hash, function hash
			jne loop_ent

			// get WinExec address
			movzx edx, word ptr[ecx + edx * 2 - 2]	// Ordinal
			mov edi, [ebp + 0x18]
			mov esi, [edi + 0x1c]					// Export Address Table
			mov edi, ebx
			add esi, edi							// Address Table
			add edi, [esi + edx * 4]
			mov eax, edi
			// edi = 함수주소 리턴
			ret

		start :
		// cmd
			xor eax, eax
			mov[ebp + 0xc], eax
			mov[ebp + 0xc], 0x63 // 0x63의 의미? 'c'
			mov[ebp + 0xd], 0x6d // 0x6d의 의미? 'm'
			mov[ebp + 0xe], 0x64 // 0x64의 의미? 'd'

		// kernel32.dll base address
			mov eax, fs:[eax + 0x30]	// eax에 저장되는 값의 의미? PEB Address 
			mov eax, [eax + 0xc]		// eax에 저장되는 값의 의미? LDR Address
			mov eax, [eax + 0x14]		// eax에 저장되는 값의 의미? LDR_DATA_TABLE_ENTRY Address (실행파일 주소) 
			mov ebx, [eax]				// ebx에 저장되는 값의 의미? LDR_DATA_TABLE_ENTRY Address (ntdll.dll 주소) 
			mov ebx, [ebx]				// ebx에 저장되는 값의 의미? LDR_DATA_TABLE_ENTRY Address (KERNEL32.dll 주소)
			mov ebx, [ebx + 0x10]		// ebx에 저장되는 값의 의미? DllBase Address

		// export table (PE구조를 참고)
			mov edi, [ebx + 0x3c]		// 0x3c의 의미? NT_HEADER로 갈 수 있는 Base 주소로부터의 Offset 값      
			add edi, ebx				// edi에 저장되는 값은 무엇을 나타내는지? NT_HEADER 시작 주소 
			mov edi, [edi + 0x78]		// 0x78의 의미? Export Table 로부터의 Offset 값 
			add edi, ebx				// edi에 저장되는 값은 무엇을 나타내는지? Export Table 시작 주소 
			mov[ebp + 0x18], edi		// Export Directory
			mov esi, [edi + 0x20]		// Export Name Table
			add esi, ebx				// esi에 저장되는 값은 무엇을 나타내는지? 함수명 배열 시작 주소 
			mov ecx, [edi + 0x24]		// 0x24의 의미?, ecx에 저장되는 값은 무엇을 나타내는지? 함수 서수 배열로 가기 위한 Offset 값까지의 Export Table 부터의 Offset 값
										// ecx -> 함수 서수 배열로 가기 위한 Offset 값 
			add ecx, ebx				// ecx에 저장되는 값은 무엇을 나타내는지? 함수 서수 배열 시작 주소 
			xor edx, edx				// ebx에 저장되는 값은? 0
			pushad						// pushad의 의미? 범용 레지스터들의 값을 스택에 넣음 

		// get WinExec addr
			xor edi, edi 
			mov di, 0x2b3
			call get_func_addr
			mov[ebp + 0x20], eax
			popad

		// get ExitProcess addr
			xor edi, edi
			add di, 0x479
			call get_func_addr
			mov[ebp + 0x24], eax

		// call WinExec
			xor eax, eax			// eax의 결과값? 0
			push eax
			lea	eax, [ebp + 0xc]	// cmd 
			push eax
			call[ebp + 0x20]		// WinExec('cmd',0)

			xor eax, eax
			push eax
			call[ebp + 0x24]		// ExitProcess(0)
	}

	return 0;
}
