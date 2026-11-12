import time
from rotary_irq_rp2 import RotaryIRQ

#necessary to change half_step in rotary_irq-rp2.py to True 

def main():
    r = RotaryIRQ(pin_num_clk=12, 
                  pin_num_dt=13, 
                  min_val=0, 
                  max_val=5, 
                  reverse=False, 
                  range_mode=RotaryIRQ.RANGE_WRAP)
                  
    val_old = r.value()
    print('initial_value', val_old)
    while True:
        val_new = r.value()
        
        if val_old != val_new:
            val_old = val_new
            print('result =', val_new)
            
        time.sleep_ms(1)
if __name__ == "__main__":
    main()
