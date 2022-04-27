const express = require("express");
const app = express();
app.use(express.json());

const {
    setCache,
    getCache
} = require('./redis');

const USER_TABLE_LIKE_DB = [];


app.get("/users/:userId", async function (req, res) {
    const userId = req.params.userId;
    
    const userCache = await getCache(userId);
    if (userCache) {
        return res.json(userCache);
    }

    const user = USER_TABLE_LIKE_DB.find(user => user.id === userId);
    if (!user) {
        return res.status(404).send();
    }
    return res.json(user);
});

app.post("/users", async function (req, res) {
    const { userId, name } = req.body;
    console.log(`>post/users/${userId}`);

    const user = {
        id: userId,
        name: name
    };

    USER_TABLE_LIKE_DB[userId] = user;
    setCache(`users${userId}`, user);
    res.send(user);
});

app.delete("/users/:userId", async function (req, res) {
    const { userId } = req.params;
    console.log(`>delete/users/${userId}`);

    delete USER_TABLE_LIKE_DB[userId];
    res.send(userId);
});

app.listen(3000);
console.log(`?listen/port/3000`);
