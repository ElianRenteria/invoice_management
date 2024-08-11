# STYLEGUIDE

## Table of Contents

1. [General Naming Conventions](#general-naming-conventions)
2. [Vue Component Guidelines](#vue-component-guidelines)
3. [Composables Usage](#composables-usage)
4. [Encapsulation of Logic](#encapsulation-of-logic)
5. [Documentation Standards](#documentation-standards)
6. [API Service Guidelines](#api-service-guidelines)
7. [File and Folder Structure](#file-and-folder-structure)
8. [Styling and CSS](#styling-and-css)

## General Naming Conventions

- **Variables**: Use `camelCase` for variables and function names.
  - Example: `userName`, `fetchData`
- **Components**: Use `PascalCase` for component names.
  - Example: `LoginView.vue`, `PrivateLayout.vue`
- **Composables**: Start the composable function names with `use` and use `camelCase`.

  - Example: `useCurrentUser`, `useClients`

- **Types/Interfaces**: Use `PascalCase` and append `Type` or `Interface` where applicable.

  - Example: `ClientType`, `UserInterface`

- **Files and Directories**: Use `PascalCase` for filenames and directories.
  - Example: `LoginView.vue`, `ClientService.ts`

## Vue Component Guidelines

- **Component Structure**: Always structure Vue components in the following order:
  1. **Template**
  2. **Script**
  3. **Style**
- **Template Structure**:
  - Use `div` containers with class bindings for structure.
  - Ensure proper nesting and alignment of template tags.
- **Props and Emitters**:
  - Define props with proper typing.
  - Emit events with clear, descriptive names.
- **Reactivity**:
  - Use `ref` and `reactive` appropriately.
  - For complex objects, prefer `reactive` to maintain reactivity of nested properties.
- **Use of Setup Script**:
  - Use `script setup` to define component logic, ensuring type safety with TypeScript.
  - Keep the logic in the script concise and modularize where possible.

## Composables Usage

- **Encapsulation**:

  - Composables should encapsulate reusable logic that is not tied to a specific component.
  - Avoid using composables to manage business logic that is highly specific to one component.

- **Return Structure**:

  - Return only what is necessary from a composable.
  - Group related reactive properties and methods together in the return object.

- **Separation of Concerns**:
  - Separate data fetching, state management, and utility logic into different composables.

## Encapsulation of Logic

- **Business Logic**:

  - Encapsulate business logic within services or composables.
  - Avoid placing business logic directly in Vue components unless it is strictly related to UI behavior.

- **UI Logic**:

  - UI-specific logic should reside within the Vue component.
  - Use composables to abstract and reuse complex UI interactions if needed.

- **Service Layers**:
  - API interactions should be encapsulated within service files.
  - Composables should interact with services rather than directly with HTTP clients.

## Documentation Standards

- **Inline Comments**:
  - Use comments to explain the reasoning behind complex or non-obvious code sections.
- **Function Documentation**:
  - Document the purpose of functions, their parameters, and return types using JSDoc/TSDoc conventions.
- **Component Documentation**:
  - Provide a brief comment at the top of each component describing its purpose and usage.

## API Service Guidelines

- **HTTP Client**:
  - Use a centralized `HttpClient` instance for making API requests.
- **Error Handling**:
  - Implement error handling within service methods and return meaningful error messages or states.
- **Type Safety**:
  - Ensure that the data returned from API requests is properly typed.
  - Use TypeScript interfaces to define the expected structure of API responses.

## File and Folder Structure

- **Views**: Should contain high-level page components that represent routes.
- **Components**: Should contain reusable UI components.
- **Composables**: Should contain reusable logic shared across multiple components.
- **Services**: Should contain business logic and API interactions.
- **Types**: Should contain TypeScript types and interfaces.

## Styling and CSS

- **Scoped Styles**:
  - Always use scoped styles within components to avoid style leakage.
- **Class Naming**:
  - Follow BEM (Block Element Modifier) conventions for naming classes.
- **Responsive Design**:
  - Utilize CSS Grid and Flexbox for layout.
  - Use utility-first CSS frameworks (like Tailwind or PrimeVue’s CSS utilities) where applicable.
