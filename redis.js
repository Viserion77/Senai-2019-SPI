const { createConnection } =require('net')
const host = 'redis-16182.c11.us-east-1-3.ec2.cloud.redislabs.com'
const port = 16182

const setCache = async (service, key, value, cacheTime = 60) => {
    await new Promise((res, rej) => {
        if (typeof value !== 'string')
            rej('Value should be a string!')

        const socket = createConnection({ host, port, })
        socket.once('connect', () => {
            socket.write({ [`${service}:${key}`]: value }, res)
        })

        socket.destroy();
        res(false)
    })
}

const getCache = async (service, key) => {
    await new Promise((res, rej) => {
        const socket = createConnection({ host, port, })
        socket.once('connect', () => {
            socket.on('data', (data) => {
                socket.destroy();
                res(data[`${service}:${key}`])
            });
        })
        socket.destroy();
        res()
    })
}

module.exports = {
    setCache,
    getCache
};