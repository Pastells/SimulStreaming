#!/usr/bin/env python3
from simulstreaming.whisper.whisper_streaming.whisper_server import main_server
from simulstreaming_whisper import simul_asr_factory, simulwhisper_args

if __name__ == "__main__":
    main_server(simul_asr_factory, add_args=simulwhisper_args)
