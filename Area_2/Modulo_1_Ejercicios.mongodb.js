/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

const database = "sample_restaurants";
const collection = "restaurants";

use(database);

db.restaurants.find();
