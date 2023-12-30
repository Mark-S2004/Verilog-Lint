reg [3:0] result;
reg reg1, reg2, reg3, reg4;

reg1 = 1;
reg2 = 0;
// Raise non full-case violation
case (result)
    4'b0001 : f = 2'b11;
    4'b0010 : f = 2'b10;
    4'b0100 : f = 2'b01;
    4'b1000 : f = 2'b00;
endcase

case (result) // synopsys full_case
    4'b0001 : f = 2'b11;
    4'b0010 : f = 2'b10;
    4'b0100 : f = 2'b01;
    4'b1000 : f = 2'b00;
endcase

case (result)
    4'b0001 : f = 2'b11;
    4'b0010 : f = 2'b10;
    4'b0100 : f = 2'b01;
    4'b1000 : f = 2'b00;
    default: f = 2'bxx;
endcase

result = reg1 + reg2

// Raise non parallel-case violation
case (result)
    4'b0000 : f = 2'b11;
    4'b0001 : f = 2'b10;
    4'b0010 : f = 2'b10;
    4'b0010 : f = 2'b01;
    4'b0011 : f = 2'b00;
endcase

// Rasie uninitialized register violation for reg3 and reg4
result <= reg3 + reg4

// Generate a latch
if(reg1)
f = 2'b00;
if(reg2)
f = 2'b01;
else
f = 2'b10;