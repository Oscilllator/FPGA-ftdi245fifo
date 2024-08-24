
# # Makefile for fpga_top_ft232h_loopback

# # Output files
# PROJ = fpga_top_ft232h_loopback
# JSON = $(PROJ).json
# ASC = $(PROJ).asc
# BIN = $(PROJ).bin

# # Source files
# SRC = fpga_ft232h_example/fpga_top_ft232h_loopback.v \
#       fpga_ft232h_example/clock_beat.v \
#       ftdi_245fifo/ftdi_245fifo_top.v \
#       ftdi_245fifo/ftdi_245fifo_fsm.v \
#       ftdi_245fifo/fifo_async.v \
#       ftdi_245fifo/fifo2.v \
#       ftdi_245fifo/fifo4.v \
#       ftdi_245fifo/resetn_sync.v \
#       ftdi_245fifo/axi_stream_assert.v \
#       ftdi_245fifo/axi_stream_downsizing.v \
#       ftdi_245fifo/axi_stream_resizing.v \
#       ftdi_245fifo/axi_stream_packing.v \
#       ftdi_245fifo/axi_stream_upsizing.v \
#       ftdi_245fifo/fifo_delay_submit.v

# # Constraint files
# PCF = fpga_ft232h_example/pins.pcf

# # FPGA settings
# DEVICE = up5k
# PACKAGE = sg48

# all: $(BIN)

# $(JSON): $(SRC)
# 	yosys -q -p "synth_ice40 -json $(JSON)" $(SRC)

# $(ASC): $(JSON) $(PCF)
# 	nextpnr-ice40 --$(DEVICE) --package $(PACKAGE) --json $(JSON) --pcf $(PCF) --asc $(ASC)

# $(BIN): $(ASC)
# 	icepack $(ASC) $(BIN)

# .PHONY: flash
# flash: $(BIN)
# 	iceprog -d i:0x0403:0x6014 $(BIN)

# .PHONY: clean
# clean:
# 	rm -f $(JSON) $(ASC) $(BIN)

# Makefile for fpga_top_ft232h_loopback

PROJ = fpga_top_ft232h_loopback
JSON = $(PROJ).json
ASC = $(PROJ).asc
BIN = $(PROJ).bin

SRC = fpga_ft232h_example/fpga_top_ft232h_loopback.v \
      fpga_ft232h_example/clock_beat.v \
      ftdi_245fifo/ftdi_245fifo_top.v \
      ftdi_245fifo/ftdi_245fifo_fsm.v \
      ftdi_245fifo/fifo_async.v \
      ftdi_245fifo/fifo2.v \
      ftdi_245fifo/fifo4.v \
      ftdi_245fifo/resetn_sync.v \
      ftdi_245fifo/axi_stream_assert.v \
      ftdi_245fifo/axi_stream_downsizing.v \
      ftdi_245fifo/axi_stream_resizing.v \
      ftdi_245fifo/axi_stream_packing.v \
      ftdi_245fifo/axi_stream_upsizing.v \
      ftdi_245fifo/fifo_delay_submit.v


PCF = fpga_ft232h_example/pins.pcf

DEVICE = up5k
PACKAGE = sg48

all: $(BIN)

$(JSON): $(SRC)
	yosys -q -p "synth_ice40 -json $(JSON)" $(SRC)

$(ASC): $(JSON) $(PCF)
	nextpnr-ice40 --$(DEVICE) --package $(PACKAGE) --json $(JSON) --pcf $(PCF) --asc $(ASC) --timing-allow-fail

$(BIN): $(ASC)
	icepack $(ASC) $(BIN)

.PHONY: flash
flash: $(BIN)
	iceprog -d i:0x0403:0x6014 $(BIN)

.PHONY: clean
clean:
	rm -f $(JSON) $(ASC) $(BIN)