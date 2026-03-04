import Events from "./pages/Events"
import Countries from "./pages/Countries"
import CountriesList from "./pages/CountriesList"
import EventsList from "./pages/EventsList"
import Home from "./pages/Home"
import "./index.css"
import MainLayout from "./layouts/MainLayout"
import { createBrowserRouter, RouterProvider } from 'react-router-dom';

const router = createBrowserRouter(
  [
    {
      path: "/", 
      element:  <MainLayout><Home/></MainLayout>
    }, 
    {
      path: "/events", 
      // loader: LoadData(self.path), 
      element:  <MainLayout><EventsList/></MainLayout>
    }, 
    {
    path: "/events/:id", 
    loader:  ({params}) => LoadData(params),  
    element: <MainLayout><Events/></MainLayout>
    },
    {
      path: "/countries", 
      // loader: async ({params}) => LoadData(params),  
      element:  <MainLayout><CountriesList/></MainLayout>
    }, 
    // {
    //   path: "/eventsList", 
    //   loader: LoadData(self.path), 
    //   element: RenderPage(<EventsList/>)
    // }, 
    //     {
    //   path: "/countriesList", 
    //   loader: LoadData(self.path), 
    //   element: RenderPage(<CountriesList/>)
    // }
  ]
)

export default function App(){
  return (<RouterProvider router={router}/>)}


async function LoadData(params){
  const apiPath = `/api/events/${params.id}`
  // if (params.id){
  //   console.log("hello")
  //   console.log(params)
  // }
  // else{
  //   console.log("what")

  // }
  // const response = fetch(apiPath)
  // response.then(response, onReject)
  try {
    const response = await fetch(apiPath)
    if (!response.ok){
      console.log(response)
      return null 
    }
    const results = await response.json()
    console.log(results)
    return (
      results
  )
  }
  catch (error){
    console.log(error)
    // TODO: Error Handler 
  }

}
