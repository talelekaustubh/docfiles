const express = require('express');
const app = express();
const port = 7000; // Port number for the application

app.get('/', (req, res) => {
  res.send('Hello World from Krishna in Docker!');
});

app.listen(port, '0.0.0.0', () => {
  console.log(`App is running on http://localhost:${port}`);
});
