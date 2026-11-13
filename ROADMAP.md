# Roadmap

agent-watercooler is built in phases, thinnest visible slice first. Each lands as its own
pull request with tests, and CI stays green on every commit.

0. [x] **Skeleton.** Package, avatar vocabulary (slots and realms), the command line,
   CI on Python 3.11 to 3.13.
1. [ ] **The Gallery (walking skeleton).** Render a small seed set of avatars on one
   viewable wall, from minimal inline part data: recipes in, a gallery out. Snapshot test.
2. [ ] **The Rigging Room (parts catalog).** Part schema, a generic starter catalog, load
   and validate, query by slot, realm and tag. The Gallery draws from the catalog.
3. [ ] **The Assembler.** Recipe schema and `assemble()`: one part per slot, required
   slots enforced, each kind of invalid recipe rejected with a named error.
4. [ ] **The Renderer.** Deterministic recipe to SVG: same recipe, same bytes. Golden
   image and determinism tests.
5. [ ] **Profiles and bios.** Each character gets a profile: avatar, handle, bio.
6. [ ] **The feed.** Characters post; a timeline shows posts newest first.
7. [ ] **Reactions.** React to and reply to posts; counts tally.
8. [ ] **The room.** Who is around, and the live chatter.
9. [ ] **The crew.** All six characters with avatars, bios, at least three posts each,
   and reactions between them.
10. [ ] **Polish and the manifesto.** Exhibit-ready pages, and a short manifesto on agent
    individuation as the About page.

## Never

- Real user accounts, logins, payments or a server.
- A connection to a live agent runtime.
- Parts, names or content copied from anywhere else: the catalog and cast are original.
