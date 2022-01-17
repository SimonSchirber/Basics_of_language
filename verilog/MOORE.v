//Mealy machine (output attached to state/inside FSM diargram bubble)
module moore_verilog_fsm(out, in rst, clk);
output out;
input in;
input clk, rst;
reg out;
reg [1:0] state; //defines how many states are present (up to ***four in this case bacuase two binary used)
parameter s0=2'd0, s1=2'd1, s2=2'd2, s3 = 2'd3;

//sequential
always @(posedge clk)
if (rst==0) begin
    state = s0;
    out = 0;
end
else begin
    case (state)
    s0: begin out = 0; 
        if (in==0) state=s0; 
        else state = s1; 
    end
    s1: begin out = 0;
        if (in == 0) state = s1;
        else state = s2 ;
    end
    s2: begin out = 0;
        if (in==0) state = s2; 
        else state = s3; 
    end
    s3: begin out = 1;
        if (in ==0) state =s3;
        else state = s0;
    end
    default: state = s0;
    endcase
end
end module
