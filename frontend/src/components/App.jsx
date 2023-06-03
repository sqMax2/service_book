import * as React  from "react";
import {Button, Table} from "react-bootstrap";
import {Route, NavLink} from "react-router-dom";
import {Routes} from "react-router";
import SwaggerUI from "swagger-ui-react";

import Auth from "./Auth";
import AnonCarInfo from "./AnonCarInfo";

import "../styles/App.css";
// import "../fonts/PT-Astra-Sans_Regular.ttf"
// import "../fonts/PT-Astra-Sans_Bold.ttf"
// import "../fonts/PT-Astra-Sans_Italic.ttf"
// import "../fonts/PT-Astra-Sans_Bold-Italic.ttf"

function App() {
    const [user, setUser] = React.useState({});

    const updateUser = (user_data) => {
        console.log('--user updated--');
        setUser(user_data);
    }

    return (
        <>
            <div className={"wrapper"}>
                <header>
                    <img alt={"Силант"} className={"logo"} src={"./media/silant/logo_main.jpg"} width={"100%"}/>
                    <div className={"contact"}><a href={"tel:+78352201209"}>+7-8352-20-12-09</a>,&nbsp;
                        <a href={"https://t.me/+78352201209"} target={"_blank"}>telegram</a></div>
                    <Auth className={"auth"} updateUser={updateUser}/>
                    <h2 className={"title"}>Электронная сервисная книжка "Мой&nbsp;Силант"</h2>
                </header>
                <main>
                    <div>Username: {user.username}, Full name: {user.first_name}. <b>Remove on prod!</b></div>
                    {!user.username ?
                        <>
                            <AnonCarInfo />
                        </> :
                        <>
                            <Routes>
                                {/*<Route path={'recipe'} element={<Categories />}>*/}
                                {/*    <Route path={':cat'} element={<Category />}>*/}
                                {/*        <Route path={':recipe'} element={<Recipe />} />*/}
                                {/*    </Route>*/}
                                {/*</Route>*/}
                                <Route path={'api-doc'} element={<SwaggerUI url="openapi" />} />
                                {/*<Route path={'/'} element={<HomePage />} />*/}
                            </Routes>
                        </>
                    }

                </main>
                <footer>
                    <div><a href={"tel:+78352201209"}>+7-8352-20-12-09</a>,&nbsp;
                        <a href={"https://t.me/+78352201209"} target={"_blank"}>telegram</a></div>
                    <div>Мой Силант 2022</div>
                </footer>
            </div>
        </>
    );
}

export default App;