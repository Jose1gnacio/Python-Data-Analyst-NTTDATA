/* global use, db */
// MongoDB Playground
// Use Ctrl+Space inside a snippet or a string literal to trigger completions.

const database = "sample_restaurants";
const collection = "restaurants";

use(database);
//db.restaurants.find();

//2.2.9
/* db.createCollection("Prueba");
db.Prueba.insertOne(
    {
        "address": {
          "building": "1234",
          "coord": [
            -73.856077,
            40.848447
          ],
          "street": "example st",
          "zipcode": "1111"
        },
        "borough": "Bronx",
        "cuisine": "Bakery",
        "grades": [
          {
            "date": {
              "$date": "2014-03-03T00:00:00Z"
            },
            "grade": "A",
            "score": 2
          },
          {
            "date": {
              "$date": "2013-09-11T00:00:00Z"
            },
            "grade": "A",
            "score": 6
          },
          {
            "date": {
              "$date": "2013-01-24T00:00:00Z"
            },
            "grade": "A",
            "score": 10
          },
          {
            "date": {
              "$date": "2011-11-23T00:00:00Z"
            },
            "grade": "A",
            "score": 9
          },
          {
            "date": {
              "$date": "2011-03-10T00:00:00Z"
            },
            "grade": "B",
            "score": 14
          }
        ],
        "name": "Morris Park Bake Shop",
        "restaurant_id": "30075445"
      }
) */

//2.2.10
//db.restaurants.find({ cuisine: "American" });

//2.2.11
/* db.restaurants.find({
  $or: [{ borough: "Brooklyn" }, { cuisine: "Italian" }],
});
let contador = db.restaurants.countDocuments({
  $or: [{ borough: "Brooklyn" }, { cuisine: "Italian" }],
});
print(
  "Cantidad de restaurants en Brooklyn o que sirven comida Italiana: " +
    contador
); */

//2.2.12
/* db.restaurants.count({
    borough: "Brooklyn", cuisine: "Italian"
}) */

//2.2.13
/* db.restaurants.find({
  borough: { $nin: ["Staten Island", "Manhattan"] },
});

db.restaurants.count({
  borough: { $nin: ["Staten Island", "Manhattan"] },
});
 */

//2.2.14
//db.restaurants.aggregate([{ $out: "restaurants_copy" }]);

//2.2.15
/* db.restaurants_copy.update(
  { name: "Carvel Ice Cream", borough: "Brooklyn" },
  { $set: { borough: "Manhattan" } }
);
db.restaurants_copy.find({ name: "Carvel Ice Cream" }); */

//2.2.16
/* db.restaurants_copy.update(
    {},
    { $set: { "cuisine": "Japanese" } }
 ) 

db.restaurants_copy.find({
    cuisine: "Japanese",
}) */

//2.2.17
/* db.restaurants_copy.deleteMany({ "borough": "Brooklyn" })

db.restaurants_copy.find({ "borough": "Brooklyn" }) */

//2.2.18
db.restaurants_copy.drop();
