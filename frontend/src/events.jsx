import { useState } from "react";

export default function Hello() {
  const [ name, setName ] = useState( "World" );

  return (
    <div>
      <h1>Hello, {name}!</h1>
      <input
        type="text"
        value={name}
        onChange={( e ) => setName( e.target.value )}
        placeholder="Enter a name"
      />
    </div>
  );
}