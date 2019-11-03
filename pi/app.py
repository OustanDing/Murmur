from microphone import MicrophoneInterface
import network

m = MicrophoneInterface()

while True:
    print("Recording...")
    m.start_streams()
    m.read_stream()
    m.write_wav()
    m.close_streams()
    network.update_file_list()
    network.print_file_list()
    print("Uploading...")
    network.upload_all(clear_after_upload = True)
