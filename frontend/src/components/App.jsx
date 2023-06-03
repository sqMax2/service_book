import * as React  from "react";
import {Button, Table} from "react-bootstrap";
import {Route, NavLink} from "react-router-dom";
import {Routes} from "react-router";
import 'bootstrap/dist/css/bootstrap.min.css';
import Auth from "./Auth";
import Main from "./Main";

import "../styles/App.css";


function App() {
    const [user, setUser] = React.useState({});

    const updateUser = (user_data) => {
        console.log('--user updated--');
        setUser(user_data);
    }
    return (
        <div className={"wrapper"}>
            <header>
                <NavLink to={'/'} className={"logo"} ><img alt={"Силант"} src={"./media/silant/logo_main.jpg"} width={"100%"}/></NavLink>
                <div className={"contact"}><a href={"tel:+78352201209"}>+7-8352-20-12-09</a>,&emsp;
                    <a href={"https://t.me/+78352201209"} target={"_blank"}>telegram</a></div>
                <Auth className={"auth"} updateUser={updateUser}/>
                <h2 className={"title"}>Электронная сервисная книжка "Мой&nbsp;Силант"</h2>
            </header>
            <main>
                <Main user={user}/>
                {/*<Routes>*/}
                {/*    <Route path={'/'} element={<Main user={user}/>} />*/}

                {/*    <Route path={'api-doc'} element={<SwaggerUI url="openapi" />}/>*/}
                {/*</Routes>*/}
            </main>
            <footer>
            <div><a href={"tel:+78352201209"}>+7-8352-20-12-09</a>,&nbsp;
                <a href={"https://t.me/+78352201209"} target={"_blank"}>telegram</a></div>
            <div>Мой Силант 2022</div>
            <NavLink to={'/api-doc'}>API</NavLink>
            </footer>
        </div>
    );
}

export default App;