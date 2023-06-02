import * as React  from "react";
import {Button} from "react-bootstrap";
import axios from "axios";
import "../styles/Auth.css";
import button from "bootstrap/js/src/button";
import {getCookie} from "./getCookie";

class Auth extends React.Component {
    constructor(props) {
        super(props);

        this.logout = this.logout.bind(this);
        this.login = this.login.bind(this);
    }

    state ={
        user: {},
    }

    componentDidMount() {
        axios.get('/api/login/')
            .then(res => {
                const user = res.data;
                // console.log('user: ', user)
                if (user.username) {
                    this.setState({user: user});
                }
                else this.setState({user: ''});
            })
    }
    componentDidUpdate(prevProps, prevState, snapshot) {
        this.props.updateUser(this.state.user);
    }

    login() {
        const username_value = document.getElementById('username').value;
        const password_value = document.getElementById('password').value;
        const csrftoken = getCookie('csrftoken');
        axios.post('/api/login/', {username: username_value, password: password_value}, {headers: {
              'Content-Type': 'application/json',
              'X-CSRFToken': csrftoken
            }})
            .then(res => {
                const user = res.data;
                if (user.username) this.setState({user: user});
                else alert('Ошибка авторизации');
            })
    }

    logout() {
        axios.get('/api/logout/')
            .then(res => {
                const response = res.data;
                // console.log('response: ', response)
                this.setState({user: ''});
            })
    }

    render () {
        return (
        <div className={this.props.className}>
            {this.state.user.username ?
                (<><div>{this.state.user.first_name ? this.state.user.first_name : this.state.user.username}</div>
                    <Button id={"logout"} onClick={this.logout}>Выйти</Button></>)
            :
                (<><input id={"username"} placeholder={"Имя пользователя"} size={"20"} maxLength={"20"} />
                <input id={"password"} placeholder={"Пароль"} size={"20"} maxLength={"20"} /> <br/>
                    <Button id={"auth-submit"} onClick={this.login}>Войти</Button></>)}

        </div>
    );
    }
}

export default Auth;