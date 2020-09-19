const express = require("express");
const mysql = require("mysql2/promise");
const app = express();

app.use(express.json());

app.get("/users", async function (req, res) {
  console.log(`>get/users/`);
  const rows = await executeSql(createQuerry("get", "users"));
  res.send(rows);
});

app.post("/users", async function (req, res) {
  console.log(`>post/users/${req.body.user}`);
  const rows = await executeSql(
    createQuerry("post", "users", { user: req.body.user }),
  );
  res.send(rows);
});

app.delete("/users", async function (req, res) {
  console.log(`>delete/users/${req.body.id}`);
  const rows = await executeSql(
    createQuerry("delete", "users", { idUsers: req.body.id }),
  );
  res.send(rows);
});

app.listen(3000);
console.log(`?listen/port/3000`);

function createQuerry(typeQuerry, table, propertys) {
  let querry = "";
  const [campos, valores] = propertys ? parsePropertysToString(propertys) : "";

  switch (typeQuerry) {
    case "get":
      querry = `SELECT * FROM ${table}`;
      break;

    case "post":
      querry = `INSERT INTO ${table} (${campos}) VALUES (${valores})`;
      break;

    case "delete":
      querry = `DELETE FROM ${table} WHERE (${campos} = ${valores});`;
      break;

    default:
      break;
  }

  return querry;

  function parsePropertysToString(propertys) {
    const propertysArray = Object.entries(propertys);
    let campos = "";
    let valores = "";

    for (const element of propertysArray) {
      let value = element[1];
      if (typeof (value) == "string") {
        value = `'${value}'`;
      }

      campos += campos == "" ? element[0] : "," + element[0];
      valores += valores == "" ? value : "," + value;
    }
    return [campos, valores];
  }
}

async function executeSql(querry) {
  console.log(`$executeSql/>${querry}`);
  //const endPoints=['users','activitys','ocnfiguration','events','locations'];
  const password = "weakpassword";
  const connection = await mysql.createConnection(
    { password, host: "localhost", user: "root", database: "senai_db" },
  );
  const [rows] = await connection.execute(querry, ["Morty", 14]);
  return rows;
}
