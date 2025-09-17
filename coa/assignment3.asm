; Assignment 3: Basic Calculator with Procedures and Stack
.MODEL SMALL
.STACK 100H
.DATA
    menu DB 'Select operation: + - * / $'
    num1 DB ?
    num2 DB ?
    result DB ?
    msg1 DB 0DH,0AH,'Enter first number: $'
    msg2 DB 0DH,0AH,'Enter second number: $'
    res_msg DB 0DH,0AH,'Result: $'
    newline DB 0DH,0AH,'$'

.CODE
MAIN PROC
    MOV AX, @DATA
    MOV DS, AX

    ; Input first number
    LEA DX, msg1
    MOV AH, 9
    INT 21H
    CALL READNUM
    MOV num1, AL

    ; Input second number
    LEA DX, msg2
    MOV AH, 9
    INT 21H
    CALL READNUM
    MOV num2, AL

    ; Show menu
    LEA DX, newline
    MOV AH, 9
    INT 21H

    LEA DX, menu
    MOV AH, 9
    INT 21H

    ; Read operation
    MOV AH, 1
    INT 21H
    MOV BL, AL

    ; Push operands to stack
    MOV AL, num1
    PUSH AX
    MOV AL, num2
    PUSH AX

    ; Decide operation
    CMP BL, '+'
    JE ADDITION
    CMP BL, '-'
    JE SUBTRACTION
    CMP BL, '*'
    JE MULTIPLICATION
    CMP BL, '/'
    JE DIVISION

ADDITION:
    POP BX
    POP AX
    ADD AL, BL
    JMP SHOW

SUBTRACTION:
    POP BX
    POP AX
    SUB AL, BL
    JMP SHOW

MULTIPLICATION:
    POP BX
    POP AX
    MUL BL
    JMP SHOW

DIVISION:
    POP BX
    POP AX
    DIV BL
    JMP SHOW

SHOW:
    ; Display result
    LEA DX, res_msg
    MOV AH, 9
    INT 21H

    ADD AL, 30H
    MOV DL, AL
    MOV AH, 2
    INT 21H

    MOV AH, 4CH
    INT 21H

; ---- Procedures ----
READNUM PROC
    MOV AH, 1
    INT 21H
    SUB AL, 30H
    RET
READNUM ENDP

MAIN ENDP
END MAIN
