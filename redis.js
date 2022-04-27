const { createConnection } = require('net')

const createRedisConnection = () => {
    return new Promise((resolve, reject) => {
        const connection = createConnection({
        host: 'localhost',
        port: 6379
        })
        connection.on('connect', () => {
            resolve(connection)
        })
        connection.on('error', reject)
    })
}

const setValue = (connection, key, value) => {
    return new Promise((resolve, reject) => {
        connection.write(`SET ${key} ${value}\r\n`, (error) => {
            if (error) {
                reject(error)
            } else {
                resolve(value)
            }
        })
    })
}

const getValue = (connection, key) => {
    return new Promise((resolve, reject) => {
        connection.write(`GET ${key}\r\n`, (error) => {
            if (error) {
                reject(error)
            } else {
                resolve(value)
            }
        })
    })
}

const setCache = async (key, value) => {
    const connection = await createRedisConnection()
    const result = await setValue(connection, key, value)
    connection.end()
    return result
}

const getCache = async (key) => {
    const connection = await createRedisConnection()
    const result = await getValue(connection, key)
    connection.end()
    return result
}

module.exports = {
    setCache,
    getCache
}
