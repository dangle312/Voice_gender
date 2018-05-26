# -*- coding: utf-8 -*-
import pyaudio
import wave

def start_record_audio_for_training_data():

	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	CHANNELS = 2
	RATE = 44100
	RECORD_SECONDS = 5
	WAVE_OUTPUT_FILENAME = "test"

	index = 0

	while True:
		p = pyaudio.PyAudio()
		stream = p.open(format=FORMAT,
					channels=CHANNELS,
					rate=RATE,
					input=True,
					frames_per_buffer=CHUNK)

		print("* start record")

		frames = []

		#frame_length = 0

		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
			data = stream.read(CHUNK)
			#frame_length += len(data)
			frames.append(data)
		#print(frame_length)
		print("* done")
		stream.stop_stream()
		stream.close()
		p.terminate()
		wf = wave.open(WAVE_OUTPUT_FILENAME + str(index) + ".wav", 'wb')
		index += 1
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(b''.join(frames))
		wf.close()
		#wait key:
		#Enter to continue recording.
		#q if want to finish.
		isContinueRecording = True
		print('Enter any key to continue, "exit" to quit')
		while True:
			name = raw_input("~/Record$ ")
			if (name == 'exit'):
				isContinueRecording = False
			break
		#to exit recording
		if (isContinueRecording == False):
			break

start_record_audio_for_training_data()