from flask import Flask, request, jsonify
import cv2
import numpy as np
app=Flask(__name__)
@app.route('api/upload',methods=['POST'])
def upload_image():
    if 'image' not in request.files:
        return jsonify({'error':'No images'}),400
    image_file=request.files['image']
    image=cv2.imdecode(np.fromstring(image_file.read().np.unit8),cv2.IMREAD_COLOR)
    processed_image=cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
    return jsonify({'processed_image':processed_image_url})
if __name__=='__main__':
    app.run(debug=True)