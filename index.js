const express = require("express");
const app = express();
app.use(express.json());

const {
    setCache,
    getCache
} = require('./redis');

const USER_TABLE_LIKE_DB = [];


app.get("/users/:userId", async function (req, res) {
    const { userId } = req.params;
    console.log(`>get/users/${userId}`);

    let user = getCache('users', userId);

    if (!user)
        user = USER_TABLE_LIKE_DB[userId];
    else user = JSON.parse(user);

    setCache('users', userId, user);
    res.send(user);
});

app.post("/users", async function (req, res) {
    const { user } = req.body;
    console.log(`>post/users/${user}`);
    
    const userId = USER_TABLE_LIKE_DB.push(user)
    setCache('users', userId, JSON.stringify(user));
    res.send(user);
});

app.delete("/users/:userId", async function (req, res) {
    const { userId } = req.params;
    console.log(`>delete/users/${userId}`);

    const value = USER_TABLE_LIKE_DB.splice(userId, 1);
    res.send(value);
});

app.listen(3000);
console.log(`?listen/port/3000`);
