ffmpeg -i /hdd/nguyenlc/hti-traffic/object_detection/test/$1.mkv -i old_model_video/$1.mp4 -i adam/$1.mp4 -i sgd/$1.mp4 \
-filter_complex "[0]drawtext=text='raw':fontsize=100:fontcolor='White':x=(w-text_w)/50:y=(h-text_h)/8[v0]; \
[1]drawtext=text='old':fontsize=100:fontcolor='White':x=(w-text_w)/50:y=(h-text_h)/8[v1]; \
[2]drawtext=text='adam':fontsize=100:fontcolor='White':x=(w-text_w)/50:y=(h-text_h)/8[v2]; \
[3]drawtext=text='sgd':fontsize=100:fontcolor='White':x=(w-text_w)/50:y=(h-text_h)/8[v3]; \
[v0][v1][v2][v3]xstack=inputs=4:layout=0_0|w0_0|0_h0|w0_h0[v]" -map "[v]" combine_video/output_$1.mp4