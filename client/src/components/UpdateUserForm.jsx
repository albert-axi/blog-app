import { useState } from "react";

function UpdateUserForm({ updateUser, onUpdateUser, onSubmitUpdateForm }) {

  const [user, setUser] = useState(updateUser)

  function handleChange(e) {
    setUser({
      ...user,
      [e.target.name]: e.target.value
    })
  }

  function handleSubmit(e) {
    e.preventDefault()

    const options = {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        'Accepts': 'application/json'
      },
      body: JSON.stringify(user)
    }

    fetch(`/users/${user.id}`, options)
      .then(res => res.json())
      .then(data => {
        onUpdateUser(data)
        onSubmitUpdateForm()
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

export default UpdateUserForm