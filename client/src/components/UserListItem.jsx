import { useState } from "react"
import { useHistory } from "react-router-dom/cjs/react-router-dom.min"
import UpdateUserForm from "./UpdateUserForm"

function UserListItem({ user, onUpdateUser, onDeleteUser }) {
  const [isUpdate, setIsUpdate] = useState(false)
  const history = useHistory()

  function onSubmitUpdateForm() {
    setIsUpdate(!isUpdate)
  }

  function handleClick(e) {
    if (e.target.name === 'update')
      setIsUpdate(!isUpdate)

    if (e.target.name === 'delete')
      fetch(`http://127.0.0.1:5555/users/${user.id}`, {
        method: "DELETE"
      })
        .then(res => res.json())
        .then(data => {
          alert(data.message)
          onDeleteUser(user)
        })

  }

  return (
    <>
      <li>
        <span onClick={() => history.push(`/users/${user.id}`, user)}>{user.email}</span>
        <button name='update' onClick={handleClick}>Update</button>
        <button name='delete' onClick={handleClick}>Delete</button>
      </li>
      {isUpdate && <UpdateUserForm onUpdateUser={onUpdateUser} updateUser={user} onSubmitUpdateForm={onSubmitUpdateForm} />}
    </>
  )
}

export default UserListItem