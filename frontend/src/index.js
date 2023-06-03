import * as React from "react";
import {createRoot} from "react-dom/client";

import {BrowserRouter, NavLink, Route} from "react-router-dom";
import App from "./components/App";
import SwaggerUI from "swagger-ui-react";
import {Routes} from "react-router";


const container = document.getElementById("root");
const root = createRoot(container);
root.render(
    <BrowserRouter>
        <Routes>
            <Route path={'/'} element={<App />} />

            <Route path={'api-doc'} element={<SwaggerUI url="openapi" />}/>
        </Routes>

        {/*<NavLink to={'/api-doc'}>API</NavLink>*/}
    </BrowserRouter>
);