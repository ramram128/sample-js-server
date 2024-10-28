const express = require('express');
const app = express();

app.use(express.json());

app.post('/receive_extracted_json', (req, res) => {
    try {
        const jsonData = req.body;


        console.log('Received JSON on port 9090:', JSON.stringify(jsonData, null, 2));

        // Extract the 'name' from the JSON structure
        const alarmResult = jsonData.alarmResult[0];
        const reserveField = alarmResult.faces[0].identify[0].candidate[0].reserve_field;
        const name = reserveField.name || 'Unknown';

        console.log(`Extracted Name: ${name}`);

        // Send the extracted name 
        res.status(200).json({ name });
    } catch (error) {
        console.error(`Error extracting name: ${error.message}`);
        res.status(400).json({ error: `Failed to extract name: ${error.message}` });
    }
});

app.listen(9090, () => {
    console.log('Server running on port 9090');
});
