const express = require("express");

const app = express();

app.set("view engine", "ejs");

app.listen(3000);

app.get("/", (req, res) => {
  res.render("index");
});

app.get("/about", (req, res) => {
  res.render("about", {
    url: req.url,
  });
});

app.get("/about-us", (req, res) => {
  res.redirect("/about");
});

app.use((req, res) => {
  res.render("404", {
    url: req.url,
  });
});
