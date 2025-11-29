```
org 100h
.data
line db '#'
crlf db 0Dh,0Ah,'$'
count db 1
.code
main proc
start:
    mov cl,count
print_hash:
    mov ah,2
    mov dl,line
    int 21h
    loop print_hash
    mov ah,9
    lea dx,crlf
    int 21h
    inc count
    cmp count,6
    jl start
    mov ah,4Ch
    int 21h
main endp
end main``` 
```

- .model small : use small memory small model 64k bytes. setup for simple 
- allocates 256 bytes for the stack, store local vars, grows down-wards
- .date: directive, set up secetion of memory to store data 
       - line db '#' : stores the # 
       - crlf db 0Dh,0Ah,'$': stores '\n'(0Dh,0Ah) and $ is a string terminator
       - count db 1: store 1 to count how many hash to print in each line

code section

- main proc: similar the main function main is the name proc is a directive to specify a start of a procedure

- start lable: the start of the loop
  - mov cl,count: loads count (1) to cl is a loop counter 
- print_hash
  -     mov ah,2 : Ah 2 charachter output ah specify wich service to call 2 is for print screen (op)
  -     mov dl,line: load # to dl  (value)
  -     int 21h: a tool to call dos functions (disk operating sys) (command)































```.model small
.stack 100h
.data
msg1 db 'Enter first digit: $'
msg2 db 0Dh,0Ah,'Enter second digit: $'
msgP db 0Dh,0Ah,'p$'
msgN db 0Dh,0Ah,'n$'
msgZ db 0Dh,0Ah,'z$'```
```

```.code
main proc
    mov ax, @data
    mov ds, ax
    ; Read first number
    mov ah, 9
    lea dx, msg1
    int 21h
    mov ah, 1
    int 21h
    cmp al, '-'
    jne positive1
    ; Handle negative first number
    mov bh, 1      ; Set sign flag
    int 21h        ; Read digit
    sub al, 30h
    mov bl, al
    jmp read_second
positive1:
    mov bh, 0      ; Clear sign flag
    sub al, 30h
    mov bl, al
read_second:
    ; Read second number
    mov ah, 9
    lea dx, msg2
    int 21h
    mov ah, 1
    int 21h
    cmp al, '-'
    jne positive2
    ; Handle negative second number
    mov ch, 1      ; Set sign flag
    int 21h        ; Read digit
    sub al, 30h
    mov cl, al
    jmp calculate
positive2:
    mov ch, 0      ; Clear sign flag
    sub al, 30h
    mov cl, al
calculate:
    ; Convert first number to two's complement
    mov al, bl
    cmp bh, 1
    jne check_second
    neg al
check_second:
    ; Convert second number and add
    mov ah, cl
    cmp ch, 1
    jne do_addition
    neg ah
do_addition:
    add al, ah
    ; Check result and print
    cmp al, 0
    jg print_positive
    jl print_negative
    ; Print zero
    mov ah, 9
    lea dx, msgZ
    int 21h
    jmp exit
print_positive:
    mov ah, 9
    lea dx, msgP
    int 21h
    jmp exit
print_negative:
    mov ah, 9
    lea dx, msgN
    int 21h
exit:
    mov ax, 4C00h
    int 21h
main endp
end main```