const express = require('express');
const axios = require('axios');
const bodyParser = require('body-parser');
const fs = require('fs');
const app = express();

// Read the API and Token
const api = fs.readFileSync('api.txt', 'utf-8').trim();
const token = fs.readFileSync('token.txt', 'utf-8').trim();

app.use(bodyParser.urlencoded({ extended: true }));
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    res.render('form');
});

app.post('/', async (req, res) => {
    const { board_id, list_name, name, desc, due, start } = req.body;

    try {
        const listsResponse = await axios.get(`https://api.trello.com/1/boards/${board_id}/lists`, {
            params: {
                key: api,
                token: token
            }
        });

        const listId = listsResponse.data.find(l => l.name === list_name)?.id;
        if (!listId) {
            return res.send(`List with the name ${list_name} not found.`);
        }

        const cardResponse = await axios.post('https://api.trello.com/1/cards', {
            name: name,
            desc: desc,
            due: due,
            start: start,
            idList: listId,
            key: api,
            token: token
        });

        if (cardResponse.status === 200) {
            res.send('Card created successfully!');
        } else {
            res.send('Failed to create the card.');
        }
    } catch (error) {
        res.send(`Error: ${error.message}`);
    }
});

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
