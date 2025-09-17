; Assignment 1: Sum of two numbers
.MODEL SMALL
.STACK 100H
.DATA
    msg1 DB 'Enter first number: $'
    msg2 DB 0DH,0AH,'Enter second number: $'
    result_msg DB 0DH,0AH,'Result: $'

    num1 DB ?
    num2 DB ?
    sum  DB ?

    p_msg DB 'p$'
    n_msg DB 'n$'
    z_msg DB 'z$'

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    ; Input first number
    LEA DX, msg1
    MOV AH, 9
    INT 21H

    MOV AH, 1       ; Read char
    INT 21H
    SUB AL, 30H     ; Convert ASCII -> digit
    MOV num1, AL

    ; Input second number
    LEA DX, msg2
    MOV AH, 9
    INT 21H

    MOV AH, 1
    INT 21H
    SUB AL, 30H
    MOV num2, AL

    ; Calculate sum
    MOV AL, num1
    ADD AL, num2
    MOV sum, AL

    ; Show result
    LEA DX, result_msg
    MOV AH, 9
    INT 21H

    ; Check sign
    CMP sum, 0
    JG POSITIVE
    JL NEGATIVE
    JE ZERO

POSITIVE:
    LEA DX, p_msg
    MOV AH, 9
    INT 21H
    JMP END_PROG

NEGATIVE:
    LEA DX, n_msg
    MOV AH, 9
    INT 21H
    JMP END_PROG

ZERO:
    LEA DX, z_msg
    MOV AH, 9
    INT 21H

END_PROG:
    MOV AH, 4CH
    INT 21H
MAIN ENDP
END MAIN
