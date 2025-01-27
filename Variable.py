import React, { useState } from 'react';
import QRCode from 'qrcode.react';

const QRGenerator = () => {
  const [inputText, setInputText] = useState('');
  const [qrValue, setQrValue] = useState('');

  const handleGenerateQR = () => {
    if (inputText.trim()) {
      setQrValue(inputText);
    }
  };

  return (
    <div className="qr-generator">
      <h1>QR Code Generator</h1>
      
      <div className="input-section">
        <input
          type="text"
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          placeholder="Enter text/URL"
        />
        <button onClick={handleGenerateQR}>Generate QR</button>
      </div>

      {qrValue && (
        <div className="qr-code">
          <QRCode
            value={qrValue}
            size={256} // Size of the QR code (pixels)
            level="H" // Error correction level (L, M, Q, H)
            fgColor="#000000" // QR code color
            bgColor="#ffffff" // Background color
            includeMargin={true} // Include white margin around QR code
          />
        </div>
      )}
    </div>
  );
};

export default QRGenerator;



.qr-generator {
  max-width: 600px;
  margin: 0 auto;
}

.input-section {
  margin: 20px 0;
}

input {
  padding: 10px;
  width: 70%;
  margin-right: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

button {
  padding: 10px 20px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}

.qr-code {
  margin-top: 20px;
  padding: 20px;
  border: 1px solid #ddd;
  border-radius: 8px;
  display: inline-block;
}
