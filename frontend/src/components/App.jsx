import * as React  from "react";
import {Button} from "react-bootstrap";
import "../styles/App.css";

import Auth from "./Auth";
// import "../fonts/PT-Astra-Sans_Regular.ttf"
// import "../fonts/PT-Astra-Sans_Bold.ttf"
// import "../fonts/PT-Astra-Sans_Italic.ttf"
// import "../fonts/PT-Astra-Sans_Bold-Italic.ttf"

function App() {
    const [user, setUser] = React.useState({});

    const updateUser = (user_data) => {
        setUser(user_data);
    }

    return (
        <>
            <div className={"wrapper"}>
                <header>
                    <img className={"logo"} src={"./media/silant/logo_main.jpg"} width={"100%"}/>
                    <div className={"contact"}>+7-8352-20-12-09, telegram</div>
                    <Auth className={"auth"} updateUser={updateUser}/>
                    <h2 className={"title"}>Электронная сервисная книжка "Мой Силант"</h2>
                </header>
                <main>
                    <h1>Съешь ещё этих мягких</h1>
                </main>
                <footer>
                    <p>+7-8352-20-12-09, telegram</p>
                    <p>Мой Силант 2022</p>
                </footer>
            </div>
        </>
    );
}

export default App;