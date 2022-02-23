const { createConnection } = require('net')
const host = 'redis-16182.c11.us-east-1-3.ec2.cloud.redislabs.com'
const port = 16182
const user = 'default'
const password = 'orO0noPT0zfOPBcxhyf2IYRIAdbwm5bp'

const setCache = async (service, key, value) => {
    await new Promise((res, rej) => {
        if (typeof value !== 'string')
            rej('Value should be a string!')

        const socket = createConnection({ host, port, })
        socket.once('connect', () => {
            socket.write('+' + JSON.stringify({ [`${service}:${key}`]: value }), res)
            socket.destroy();
        })
        res(false)
    })
}
setCache('1', '2', '3')

const getCache = async (service, key) => {
    await new Promise((res, rej) => {
        const socket = createConnection({ host, port, })
        socket.once('connect', () => {
            socket.on('data', (data) => {
                res(JSON.parse(data[`${service}:${key}`]))
                socket.destroy();
            });
        })
        res()
    })
}

getCache('1', '2')
module.exports = {
    setCache,
    getCache
};