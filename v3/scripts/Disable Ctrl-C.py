# disable accidental Ctrl-C key press from shutting down the engine
signal.signal(signal.SIGINT, signal.SIG_IGN)