module Top();
    reg [7:0] reg1;
    reg [1:0] f;
    reg [3:0] result ;
    result = 4'b0101;

    always @(posedge clk or posedge rst) begin
        if (rst) begin
            reg1 <= 8'b00000000;
            reg2 <= 8'b11110000;
        end else begin
            reg1 <= data_in + reg2;
            reg2 <= reg1;
        end

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

        // reg3 is uninitialized in this block
        result <= reg1 + reg2;
    end

    always @(posedge clk) begin
        // reg3 is uninitialized in this block
        data_out <= result + reg3;

        // Raise non full-case violation
        case (result)
            4'b0001 : f = 2'b11;
            4'b0010: f=2'b10;
            4'b0100 :f =2'b01;
            4'b1000 :  f = 2'b00;
        endcase
    end
endmodule