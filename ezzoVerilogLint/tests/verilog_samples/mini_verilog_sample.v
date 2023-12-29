reg [3:0] result;

// Raise non full-case violation
case (result)
    4'b0001 : f = 2'b11;
    4'b0010: f=2'b10;
    4'b0100 :f =2'b01;
    4'b1000 :  f = 2'b00;
endcase

case (result) // synopsys full_case
    4'b0001 : f = 2'b11;
    4'b0010: f=2'b10;
    4'b0100 :f =2'b01;
    4'b1000 :  f = 2'b00;
endcase

case (result)
    4'b0001 : f = 2'b11;
    4'b0010: f=2'b10;
    4'b0100 :f =2'b01;
    4'b1000 :  f = 2'b00;
    default:f= 2'bxx;
endcase