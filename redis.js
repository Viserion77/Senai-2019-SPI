const redis = require('promise-redis');
const client = redis.createClient();

const setCache = async (service, key, value, cacheTime = 60) => {
    if (typeof value !== 'string')
        throw new Error('Value should be a string!')
    const result = await client.set(`${service}:${key}`, value, 'EX', cacheTime);

    return result === 'OK'
}

const getCache = async (service, key) => client.get(`${service}:${key}`);

module.exports = {
    setCache,
    getCache
};