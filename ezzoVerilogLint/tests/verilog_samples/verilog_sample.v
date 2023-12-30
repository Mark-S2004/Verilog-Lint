module Top();
    reg [7:0] reg1;
    reg [7:0] reg2;
    reg [1:0] f;
    reg [3:0] result ;
    reg a, b, c, d;
    result = 4'b0101;

    always @(posedge clk or posedge rst) begin
        // Raise uninitialized register violation for register b
        a <= b;

        if (rst) begin
            reg1 <= 8'b00000000;
            reg2 <= 8'b11110000;
        end else begin
            // raise uninitialized reg for data_in
            reg1 <= data_in + reg2;
            reg2 <= reg1;
        end

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
        

        // Generate a latch
        if(reg1)
        f = 2'b00;
        else if(reg2)
        f = 2'b01;

        // reg3 is uninitialized in this block
        result <= reg1 + reg2;
    end

    always @(posedge clk) begin
        // Raise uninitialized register violation for register c
        b <= c;

        // reg3 is uninitialized in this block
        data_out <= result + reg3;

        // Raise non full-case violation
        case (result)
            4'b0001 : f = 2'b11;
            4'b0010 : f = 2'b10;
            4'b0100 : f = 2'b01;
            4'b1000 : f = 2'b00;
        endcase

        // Raise non parallel-case violation
        case (result)
            4'b0000 : f = 2'b11;
            4'b0001 : f = 2'b10;
            4'b0010 : f = 2'b10;
            4'b0010 : f = 2'b01;
            4'b0011 : f = 2'b00;
        endcase
    end

    always @(posedge clk)
    begin
        // raise uninitialized reg for d
        b <= d;
    end

    
    input wire [2:0] reg_input_00,reg_input_01;
    output wire [2:0] reg_result_0;


    input wire [9:0] reg_input_1,reg_input_2;
    output wire [2:0] reg_result_1;

    input reg [3:0] reg_11,reg_22;
    output reg [1:0] reg_result_2;

    wire [5:0] reg_input_3,reg_input_4;
    wire [2:0] reg_result_3;

    reg [5:0] reg_input_5,reg_input_6;
    reg [2:0] reg_result_4;

    // No Arithmetic overflow
    reg_result_0 = reg_input_00 + reg_input_01

    // Arithmetic overflow
    reg_result_1 = reg_input_1 + reg_input_2

    // Arithmetic overflow
    reg_result_2 = reg_11 + reg_22

    // Arithmetic overflow
    reg_result_3 = reg_input_3 + reg_input_4

    // Arithmetic overflow
    reg_result_4 = reg_input_5 + reg_input_6



endmodule


