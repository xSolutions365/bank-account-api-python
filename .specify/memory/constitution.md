<!--
Sync Impact Report:
Version: N/A → 1.0.0 (Initial constitution)
Modified Principles: N/A (Initial version)
Added Sections: All sections created from template
Removed Sections: None
Templates Status:
  ✅ plan-template.md - Reviewed, no updates needed (already includes Constitution Check section)
  ✅ spec-template.md - Reviewed, aligns with testing and requirements principles
  ✅ tasks-template.md - Reviewed, aligns with testing discipline and phased approach
Follow-up TODOs: None
-->

# Bank Account Solution Constitution

## Core Principles

### I. Separation of Concerns (MVC Architecture)

Code MUST be organized following the Model-View-Controller pattern:
- **Models** define data structures and validation logic only
- **Services** contain business logic and data manipulation
- **Controllers** handle HTTP routing and request/response formatting
- Each layer MUST have clear boundaries with minimal coupling
- Cross-cutting concerns (logging, error handling) MUST be extracted to shared utilities

**Rationale**: Clear separation enables independent testing of business logic, easier maintenance, and parallel development of frontend and backend teams.

### II. Comprehensive Testing (NON-NEGOTIABLE)

All code MUST be covered by appropriate tests before merging:
- **Unit tests**: Required for all service and model classes (target: 80%+ coverage)
- **Integration tests**: Required for controller endpoints testing full request/response cycle
- **E2E tests**: Required for critical user journeys across frontend and backend
- Tests MUST be written in this order: failing tests first, then implementation
- All tests MUST pass in CI before merge

**Rationale**: Testing discipline prevents regressions, documents expected behavior, and enables confident refactoring. The test-first approach ensures testability and clearer requirements.

### III. Code Quality Standards

All code MUST meet automated quality gates before merge:
- **Backend (Python)**: black (formatting), flake8 (linting), mypy (type checking), pytest (tests)
- **Frontend (TypeScript/React)**: eslint (linting), TypeScript strict mode (type safety), Mocha (tests)
- No warnings or errors from quality tools allowed in main branch
- Line length: 100 characters (Python), standard for TypeScript
- Type hints required for all Python function signatures

**Rationale**: Consistent code quality reduces cognitive load, catches bugs early, and ensures maintainability across team members.

### IV. API-First Design

Backend and frontend MUST be developed as independent, loosely coupled applications:
- REST API contract defined before implementation begins
- Backend exposes JSON REST endpoints at `/api/*` namespace
- Frontend consumes backend only through documented API endpoints
- No direct database or service access from frontend
- API versioning MUST be considered for breaking changes

**Rationale**: API-first design enables parallel development, clear contracts, easier testing, and potential for multiple frontend implementations or third-party integrations.

### V. Dependency Management and Reproducibility

All dependencies MUST be explicitly versioned and reproducible:
- **Backend**: Poetry preferred (pyproject.toml), requirements.txt maintained for compatibility
- **Frontend**: npm with package-lock.json committed
- Version pinning: Minor/patch versions locked (e.g., `fastapi = "^0.115.0"`)
- No global installations required; all tools run within project environment
- README MUST document all prerequisites (Python 3.9+, Node.js 18+)

**Rationale**: Version locking prevents "works on my machine" issues, ensures reproducible builds, and enables reliable CI/CD pipelines.

## Technology Stack Constraints

### Approved Technologies

**Backend Stack**:
- **Language**: Python 3.9 or higher
- **Web Framework**: FastAPI with Uvicorn
- **Testing**: pytest, pytest-cov, pytest-asyncio, httpx
- **Code Quality**: black, flake8, mypy
- **Package Management**: Poetry (primary), pip (fallback)

**Frontend Stack**:
- **Language**: TypeScript 5.7+
- **Framework**: React 19+ with hooks-based components
- **Build Tool**: Vite 6+
- **UI Library**: Material-UI (MUI) 6+, Emotion for styling
- **Routing**: React Router 7+
- **HTTP Client**: Axios
- **Testing**: Mocha, Chai, Selenium WebDriver

**Version Control and Branching**:
- Feature branches MUST follow format: `###-feature-name`
- All work MUST be done on feature branches, not main
- Specifications stored in `specs/[###-feature-name]/` structure

### Technology Change Policy

Introducing new major frameworks or tools requires:
1. Written justification addressing why current stack insufficient
2. Proof of concept demonstrating value
3. Migration plan if replacing existing technology
4. Update to this constitution documenting the change

Minor libraries (utilities, helpers) can be added freely if they:
- Serve a clear, specific purpose
- Don't duplicate existing functionality
- Are actively maintained with good community support

## Development Workflow

### Project Structure Requirements

**Repository Organization**:
```
bank-account-api-py/    # Backend Python application
  app/                  # Application source code
    [feature]/          # Feature modules (MVC structure)
  tests/                # Test suite
    unit/              # Unit tests
    e2e/               # End-to-end tests
  pyproject.toml        # Poetry dependencies
  requirements.txt      # Pip dependencies

bank-account-ui/        # Frontend React application
  src/                  # Application source code
    components/         # Reusable UI components
    pages/             # Page-level components
    api/               # API client code
  test/                 # Test suite
  package.json          # npm dependencies

specs/                  # Feature specifications (if using speckit)
  [###-feature]/        # Per-feature documentation
    plan.md
    spec.md
    tasks.md
```

### Feature Development Process

**Standard Feature Flow**:
1. **Specification**: Document user stories, requirements, acceptance criteria in `specs/[###-feature]/spec.md`
2. **Planning**: Create implementation plan in `specs/[###-feature]/plan.md` with technical approach
3. **Test Writing**: Write failing tests for each user story (unit → integration → e2e)
4. **Implementation**: Implement feature to make tests pass
5. **Quality Gates**: Ensure all quality checks pass (linting, types, tests, coverage)
6. **Review**: Code review with constitution compliance check
7. **Integration**: Merge to main after approval

**Constitution Compliance Checklist** (per feature):
- [ ] Tests written before implementation and initially failed
- [ ] All tests passing (unit, integration, e2e as appropriate)
- [ ] Code quality tools pass with no warnings
- [ ] MVC separation maintained
- [ ] API contracts documented
- [ ] Dependencies explicitly versioned
- [ ] README updated if new setup steps required

### Testing Discipline

**Test Coverage Requirements**:
- Services: 80%+ line coverage minimum
- Models: 100% method coverage (models should be simple)
- Controllers: Full endpoint coverage with status code verification
- E2E: Cover all critical user paths end-to-end

**Test Independence**:
- Unit tests MUST NOT depend on external services or databases
- Integration tests MUST reset state between tests (use fixtures)
- E2E tests MUST be runnable independently in any order

## Governance

**Constitution Authority**:
- This constitution supersedes all other development practices and guidelines
- All pull requests MUST be reviewed for constitutional compliance
- Any complexity or deviations MUST be explicitly justified in implementation plans
- Constitution violations without justification are grounds for PR rejection

**Amendment Process**:
1. Propose amendment with clear rationale in GitHub issue or PR
2. Document what is changing and why current principle is insufficient
3. Update constitution version following semantic versioning:
   - **MAJOR**: Backward-incompatible changes (principle removal, redefinition)
   - **MINOR**: New principles or materially expanded guidance
   - **PATCH**: Clarifications, wording improvements, non-semantic changes
4. Update `LAST_AMENDED_DATE` to date of merge
5. Propagate changes to affected templates (plan, spec, tasks)
6. Announce amendment to team with migration guidance if needed

**Version History**:
- All constitutional amendments MUST maintain version history
- Sync Impact Report MUST be added as HTML comment at file top
- Breaking changes MUST include migration path for existing features

**Compliance Review**:
- Constitution compliance checked during code review
- Quarterly review of constitution relevance and effectiveness
- Metrics tracked: test coverage, code quality tool pass rate, constitutional violations

**Version**: 1.0.0 | **Ratified**: 2026-01-14 | **Last Amended**: 2026-01-14
