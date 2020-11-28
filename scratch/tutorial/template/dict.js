document.getElementById("dict-full").innerHTML = `
when flag clicked
set [name] [Peter]
get [name] [none]
say (get-output) for (3) seconds // says "Peter"
delete [name]
get [name] [none]
say (get-output) for (3) seconds // says "none"

define setup // can be merged into the main thread
delete all of [dict v]
set [get-index v] to (0)
set [set-index v] to (0)
set [delete-index v] to (0)

define get (key) (default)
repeat until <(get-index)=(0)>
end
set [get-index v] to (1)
forever
  if <(get-index)>(length of [dict v])> then
    set [get-output v] to (default)
    set [get-index v] to (0)
    stop [this script v]
  end
  if <(item (get-index) of [dict v])=(key)> then
    set [get-output v] to (item ((get-index)+(1)) of [dict v])
    set [get-index v] to (0)
    stop [this script v]
  end
  change [get-index v] by (2)

define set (key) (value)
repeat until <(set-index)=(0)>
end
set [set-index v] to (1)
forever
  if <(set-index)>(length of [dict v])> then
    add (key) to [dict v]
    add (value) to [dict v]
    stop [this script v]
  end
  if <(item (set-index) of [dict v])=(key)> then
    replace item ((set-index)+(1)) of [dict v] with (value)
    stop [this script v]
  end
  change [set-index v] by (2)


define delete (key)
set [delete-index v] to (1)
forever
  if <(delete-index)>(length of [dict v])> then
    stop [this script v]
  end
  if <(item (delete-index) of [dict v])=(key)> then
    delete (delete-index) of [dict v]
    delete (delete-index) of [dict v]
    stop [this script v]
  end
  change [delete-index v] by (2)
`