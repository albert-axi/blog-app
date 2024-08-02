import { useState } from "react";

const initialUser = {
  username: "",
  email: "",
  mobile_number: ""
}

function AddUserForm({ onAddUser }) {
  const [user, setUser] = useState(initialUser)

  function handleChange(e) {
    setUser({
      ...user,
      [e.target.name]: e.target.value
    })
  }

  function handleSubmit(e) {
    e.preventDefault()

    const options = {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accepts': 'application/json'
      },
      body: JSON.stringify(user)
    }

    fetch('/users', options)
      .then(res => res.json())
      .then(data => {
        onAddUser(data)
        setUser(initialUser)
      })
  }

  return (
    <form onSubmit={handleSubmit}>
      <input type="text" name="username" value={user.username} onChange={handleChange} placeholder="username" /><br />
      <input type="text" name="email" value={user.email} onChange={handleChange} placeholder="email" /><br />
      <input type="text" name="mobile_number" value={user.mobile_number} onChange={handleChange} placeholder="mobile_number" /><br />
      <input type="submit" />
    </form>
  )
}

export default AddUserForm