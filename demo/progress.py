"""Independent learning-progress example using synthetic module IDs."""
def progress(modules: list[str], completed: list[str]) -> dict:
    if not modules or any(not isinstance(m, str) or not m.strip() for m in modules) or len(set(modules)) != len(modules):
        raise ValueError("Provide unique, nonempty module identifiers")
    done = set(completed)
    if not done <= set(modules):
        raise ValueError("Unknown completed module")
    return {"completed": len(done), "total": len(modules), "percent": 100*len(done)/len(modules), "next": next((m for m in modules if m not in done), None)}

if __name__ == "__main__":
    print(progress(["intro","practice","review"], ["intro"]))
