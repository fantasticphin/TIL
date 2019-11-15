const trips = [
  {distance: 34, time: 10},
  {distance: 90, time: 50},
  {distance: 59, time: 20},
]

const speeds = trips.map(function(trip){
  return {speed: trip.distance / trip.time}
})

console.log(speeds)