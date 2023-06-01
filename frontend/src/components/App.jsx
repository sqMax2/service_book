import * as React  from "react";
import {Button} from "react-bootstrap";
import "../styles/App.css";
// import "../fonts/PT-Astra-Sans_Regular.ttf"
// import "../fonts/PT-Astra-Sans_Bold.ttf"
// import "../fonts/PT-Astra-Sans_Italic.ttf"
// import "../fonts/PT-Astra-Sans_Bold-Italic.ttf"

function App() {
    return (
        <>
            <div className={"wrapper"}>
                <header>
                    <img className={"logo"} src={"./media/silant/logo_main.jpg"} width={"200vw"}/>
                    <div>+7-8352-20-12-09, telegram</div>
                    <Button>авторизация</Button>
                    <h2>Электронная сервисная книжка "Мой Силант"</h2>
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