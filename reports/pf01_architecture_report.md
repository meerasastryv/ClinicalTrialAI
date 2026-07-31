# ClinicalTrialAI Architecture Report

**Engine** : PF01-DEMO

**Health Score** : 65.0/100
**Rating** : Needs Improvement

## Dependency Summary

- Total Dependencies : 10
- Internal : 0
- External : 10
- Standard Library : 0

## Circular Dependencies

- moduleA -> moduleB -> moduleC -> moduleA

## Top Fan-Out

- service.user_service: 3
- controller.user_controller: 2
- repository.user_repository: 2
- moduleA: 1
- moduleB: 1
- moduleC: 1

## Top Fan-In

- service.user_service: 1
- repository.user_repository: 1
- database.connection: 1
- utils.validator: 1
- utils.logger: 1
- dto.user_dto: 1
- models.user: 1
- moduleB: 1
- moduleC: 1
- moduleA: 1

## Dependency Intelligence

### Architectural Hotspots

- moduleA
  - Score : 22
  - FanIn=1, FanOut=1, Cycle=True
- moduleB
  - Score : 22
  - FanIn=1, FanOut=1, Cycle=True
- moduleC
  - Score : 22
  - FanIn=1, FanOut=1, Cycle=True

### Module Metrics

#### service.user_service
- Fan In : 1
- Fan Out : 3
- Instability : 0.75
- Risk : LOW
- In Cycle : False

#### repository.user_repository
- Fan In : 1
- Fan Out : 2
- Instability : 0.67
- Risk : LOW
- In Cycle : False

#### controller.user_controller
- Fan In : 0
- Fan Out : 2
- Instability : 1.0
- Risk : LOW
- In Cycle : False

#### moduleA
- Fan In : 1
- Fan Out : 1
- Instability : 0.5
- Risk : CRITICAL
- In Cycle : True

#### moduleB
- Fan In : 1
- Fan Out : 1
- Instability : 0.5
- Risk : CRITICAL
- In Cycle : True

#### moduleC
- Fan In : 1
- Fan Out : 1
- Instability : 0.5
- Risk : CRITICAL
- In Cycle : True

#### dto.user_dto
- Fan In : 1
- Fan Out : 0
- Instability : 0.0
- Risk : LOW
- In Cycle : False

#### utils.validator
- Fan In : 1
- Fan Out : 0
- Instability : 0.0
- Risk : LOW
- In Cycle : False

#### utils.logger
- Fan In : 1
- Fan Out : 0
- Instability : 0.0
- Risk : LOW
- In Cycle : False

#### database.connection
- Fan In : 1
- Fan Out : 0
- Instability : 0.0
- Risk : LOW
- In Cycle : False

#### models.user
- Fan In : 1
- Fan Out : 0
- Instability : 0.0
- Risk : LOW
- In Cycle : False

### Intelligence Cycles

- moduleA -> moduleB -> moduleC -> moduleA

### Intelligence Recommendations

- Break circular dependencies.
- Refactor architectural hotspots.

## Warnings

- Circular dependencies detected.
- High external dependency ratio.

## Recommendations

- Review architecture for coupling and dependency improvements.
