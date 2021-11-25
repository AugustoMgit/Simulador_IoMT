// import axios from 'axios';

// const restApi = axios.create({
//     baseUrl: "http://"
// });


const users = [
    {
        name: 'joao',
        birthday: '2007-11-09',
        gender: 'M'
    },
    {
        name: 'maria',
        birthday: '2002-11-09',
        gender: 'F'
    },
    {
        name: 'roberson',
        birthday: '1992-11-09',
        gender: 'M'
    }
]

var api = {

    users: {
        getAllUsers() {
            return users;
        },
        registerNewUser(newUser) {
            return users.push(newUser);
        }
    }

}

export default api;
