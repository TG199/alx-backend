#!/usr/bin/node
import redis from "redis";
import { promisify} from 'util';

const client = redis.createClient();

const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
    console.log('Redis client connected to the server');
});
client.on('error', () => {
    console.console.log('Redis client not connected to the server: ERROR_MESSAGE');
});

const setNewSchool = (schoolName, value) => {
    client.set(schoolName, value);
    redis.print(`Successfully set the value ${schoolName}`);
}

const displaySchoolValue = (schoolName) => {
    client.get(schoolName, (err, reply) => {
        if (err) {
          console.error(`Error retrieving value: ${err.message}`);
        } else {
          console.log(reply);
        }
      });
}
displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');