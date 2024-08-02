import { useEffect, useState } from "react";
import AddUserForm from "./AddUserForm";
import UserListItem from "./UserListItem";

function UserPage() {

  const [users, setUsers] = useState([])

  useEffect(() => {
    fetch('/users')
      .then(res => res.json())
      .then(data => setUsers(data))

  }, [])

  function onAddUser(user) {
    setUsers([...users, user])
  }

  function onUpdateUser(user) {
    setUsers(users.map(u => {
      if (u.id === user.id)
        return user

      return u
    }))
  }

  function onDeleteUser(user) {
    setUsers(users.filter(u => u.id !== user.id))
  }

  return (
    <div>
      <h2>User Page</h2>
      <AddUserForm onAddUser={onAddUser} />
      <ul>
        {users.map((user, i) => <UserListItem key={i} onUpdateUser={onUpdateUser} onDeleteUser={onDeleteUser} user={user} />)}
      </ul>
    </div>
  )
}

export default UserPage