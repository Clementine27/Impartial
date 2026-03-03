import Header from "../components/Header"
import "./MainLayout.css"

export default function MainLayout({children}){
    return (
        <div className="app-layout">
            <div className="app-header">
                <Header/>
            </div>

            <div className="app-body">
                {children}
            </div>
        </div>
    )
}

